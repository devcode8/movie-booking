# Movie Ticket Booking System

This project implements a movie ticket booking system using AI agents. It allows users to book and unbook movie tickets as well as view the movie schedule. The system comprises a theater agent that manages the movie schedule and a user agent that interacts with the user to book or unbook tickets.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Agents and Protocols](#agents-and-protocols)
4. [Running the Agents](#running-the-agents)
5. [Example Interactions](#example-interactions)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/devcode8/movie-booking.git
    cd movie-booking
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the theater agent:

    ```bash
    python movie_theater.py
    ```
2. Copy the movie_theater agent address to user agent:

    ```bash
    THEATER_AGENT_ADDRESS = "agent1q22q78dcc8twwk4gfqqql9za8ae5wsx2ednqccdfrp74mx25g4tz62geqxv"
    ```

2. In a separate terminal, start the user agent:

    ```bash
    python user.py
    ```

3. Follow the on-screen prompts to interact with the system.

## Agents and Protocols

### Protocols

The protocols define the structure of the messages exchanged between the user and theater agents.

- `QueryScheduleRequest` and `QueryScheduleResponse`: Used to request and respond with the current movie schedule.
- `BookTicketRequest` and `BookTicketResponse`: Used to book a ticket for a specified movie and time.
- `UnbookTicketRequest` and `UnbookTicketResponse`: Used to unbook a previously booked ticket.

### Theater Agent

The theater agent (`movie_theater.py`) manages the movie schedule and handles booking and unbooking requests.

### User Agent

The user agent (`user.py`) interacts with the user to facilitate booking and unbooking tickets and viewing the schedule.

## Running the Agents

1. **Theater Agent**: 

    The theater agent initializes with a predefined movie schedule and listens for requests from the user agent.

    ```python
    python movie_theater.py
    ```

2. **User Agent**:

    The user agent presents a menu to the user, allowing them to book tickets, unbook tickets, or view the schedule.

    ```python
    python user.py
    ```

## Example Interactions

### Booking a Ticket

1. The user agent presents a menu:
    ```
    What would you like to do?
    1. Book a movie ticket
    2. Unbook a movie ticket
    3. Display movie schedule
    4. Exit
    Enter the number of your choice: 
    ```

2. The user chooses to book a ticket (`1`).

3. The user enters the movie name and preferred show time.

4. The system attempts to book the ticket and notifies the user of the success or failure.

### Unbooking a Ticket

1. The user agent presents a menu:
    ```
    What would you like to do?
    1. Book a movie ticket
    2. Unbook a movie ticket
    3. Display movie schedule
    4. Exit
    Enter the number of your choice: 
    ```

2. The user chooses to unbook a ticket (`2`).

3. The user enters the movie name and show time.

4. The system attempts to unbook the ticket and notifies the user of the success or failure.

### Viewing the Schedule

1. The user agent presents a menu:
    ```
    What would you like to do?
    1. Book a movie ticket
    2. Unbook a movie ticket
    3. Display movie schedule
    4. Exit
    Enter the number of your choice: 
    ```

2. The user chooses to view the schedule (`3`).

3. The system displays the current movie schedule with available seats for each time slot.

### Exiting

1. The user agent presents a menu:
    ```
    What would you like to do?
    1. Book a movie ticket
    2. Unbook a movie ticket
    3. Display movie schedule
    4. Exit
    Enter the number of your choice: 
    ```

2. The user chooses to exit (`4`).

3. The user agent stops running.

---
### Author : Dev Chauhan
### Follow [Linkedin](https://tr.ee/_PmCkGvdRy) | [Instagram](https://www.instagram.com/_unknown_code__/)
