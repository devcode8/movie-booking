from uagents import Context, Model, Protocol

class MovieSchedule(Model):
    movies: dict

class QueryScheduleRequest(Model):
    pass

class QueryScheduleResponse(Model):
    schedule: dict

class BookTicketRequest(Model):
    movie: str
    time: str

class BookTicketResponse(Model):
    success: bool
    movie: str
    time: str

class UnbookTicketRequest(Model):
    movie: str
    time: str

class UnbookTicketResponse(Model):
    success: bool
    movie: str
    time: str

movie_proto = Protocol()

@movie_proto.on_message(model=QueryScheduleRequest, replies=QueryScheduleResponse)
async def handle_query_schedule(ctx: Context, sender: str, msg: QueryScheduleRequest):
    schedule = ctx.storage.get("schedule")
    if schedule is None:
        schedule = {}
    await ctx.send(sender, QueryScheduleResponse(schedule=schedule))

@movie_proto.on_message(model=BookTicketRequest, replies=BookTicketResponse)
async def handle_book_ticket(ctx: Context, sender: str, msg: BookTicketRequest):
    schedule = ctx.storage.get("schedule")
    if schedule is None:
        schedule = {}

    movie = msg.movie
    time = msg.time

    if movie in schedule and time in schedule[movie]:
        if schedule[movie][time] > 0:
            schedule[movie][time] -= 1
            ctx.storage.set("schedule", schedule)
            await ctx.send(sender, BookTicketResponse(success=True, movie=movie, time=time))
            return
    await ctx.send(sender, BookTicketResponse(success=False, movie=movie, time=time))

@movie_proto.on_message(model=UnbookTicketRequest, replies=UnbookTicketResponse)
async def handle_unbook_ticket(ctx: Context, sender: str, msg: UnbookTicketRequest):
    schedule = ctx.storage.get("schedule")
    if schedule is None:
        schedule = {}

    movie = msg.movie
    time = msg.time

    if movie in schedule and time in schedule[movie]:
        schedule[movie][time] += 1
        ctx.storage.set("schedule", schedule)
        await ctx.send(sender, UnbookTicketResponse(success=True, movie=movie, time=time))
        return
    await ctx.send(sender, UnbookTicketResponse(success=False, movie=movie, time=time))
