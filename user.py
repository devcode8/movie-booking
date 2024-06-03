from protocols.movie_booking import (
    QueryScheduleRequest,
    QueryScheduleResponse,
    BookTicketRequest,
    BookTicketResponse,
    UnbookTicketRequest,
    UnbookTicketResponse,
)
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low

THEATER_AGENT_ADDRESS = "agent1q22q78dcc8twwk4gfqqql9za8ae5wsx2ednqccdfrp74mx25g4tz62geqxv"

user = Agent(
    name="user",
    port=8000,
    seed="user secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(user.wallet.address())

async def get_user_choice():
    print("What would you like to do?")
    print("1. Book a movie ticket")
    print("2. Unbook a movie ticket")
    print("3. Display movie schedule")
    print("4. Exit")
    return int(input("Enter the number of your choice: "))

async def book_ticket(ctx: Context):
    movie = input("Enter the movie name: ")
    time = input("Enter the preferred show time: ")

    ctx.storage.set("movie", movie)
    ctx.storage.set("time", time)

    book_request = BookTicketRequest(movie=movie, time=time)
    await ctx.send(THEATER_AGENT_ADDRESS, book_request)

async def unbook_ticket(ctx: Context):
    movie = input("Enter the movie name: ")
    time = input("Enter the show time: ")

    unbook_request = UnbookTicketRequest(movie=movie, time=time)
    await ctx.send(THEATER_AGENT_ADDRESS, unbook_request)

async def display_schedule(ctx: Context):
    schedule_request = QueryScheduleRequest()
    await ctx.send(THEATER_AGENT_ADDRESS, schedule_request)

@user.on_interval(period=3.0)
async def interval(ctx: Context):
    if not ctx.storage.get("waiting_for_response"):
        choice = await get_user_choice()
        ctx.storage.set("completed", False)

        if choice == 1:
            await book_ticket(ctx)
        elif choice == 2:
            await unbook_ticket(ctx)
        elif choice == 3:
            await display_schedule(ctx)
        elif choice == 4:
            print("Exiting...")
            ctx.storage.set("exit", True)
            return
        else:
            print("Invalid choice.")

        ctx.storage.set("waiting_for_response", True)

@user.on_message(QueryScheduleResponse, replies=set())
async def handle_query_schedule_response(ctx: Context, sender: str, msg: QueryScheduleResponse):
    print("Movie Schedule:")
    for movie, times in msg.schedule.items():
        print(f"{movie}:")
        for time, seats in times.items():
            print(f"  {time} - {seats} seats available")
    ctx.storage.set("waiting_for_response", False)

@user.on_message(BookTicketResponse, replies=set())
async def handle_book_ticket_response(ctx: Context, _sender: str, msg: BookTicketResponse):
    if msg.success:
        ctx.logger.info(f"Successfully booked ticket for {msg.movie} at {msg.time}")
    else:
        ctx.logger.info(f"Failed to book ticket for {msg.movie} at {msg.time}")
    ctx.storage.set("waiting_for_response", False)

@user.on_message(UnbookTicketResponse, replies=set())
async def handle_unbook_ticket_response(ctx: Context, _sender: str, msg: UnbookTicketResponse):
    if msg.success:
        ctx.logger.info(f"Successfully unbooked ticket for {msg.movie} at {msg.time}")
    else:
        ctx.logger.info(f"Failed to unbook ticket for {msg.movie} at {msg.time}")
    ctx.storage.set("waiting_for_response", False)

if __name__ == "__main__":
    user.run()
