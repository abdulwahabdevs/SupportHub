from datetime import datetime
from .store import tickets, _ticket_id_counter


def create_ticket(data, user):
    ticket_id = next(_ticket_id_counter)

    ticket = {
        "id": ticket_id,
        "question": data["question"],
        "status": "open",
        "owner": user["id"],
        "assigned_agent_id": None,
        "created_at": datetime.utcnow().isoformat()
    }

    tickets[ticket_id] = ticket
    return ticket_id
