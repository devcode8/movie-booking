from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from protocols.movie_booking import movie_proto, MovieSchedule

theater = Agent(
    name="theater",
    port=8001,
    seed="theater secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(theater.wallet.address())

theater.include(movie_proto)

MOVIE_SCHEDULE = {
    "Movie A": {"10:00": 50, "13:00": 50, "16:00": 50},
    "Movie B": {"11:00": 50, "14:00": 50, "17:00": 50},
    "Movie C": {"12:00": 50, "15:00": 50, "18:00": 50},
}

theater._storage.set("schedule", MOVIE_SCHEDULE)

if __name__ == "__main__":
    theater.run()
