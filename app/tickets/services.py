def create_ticket(data, user):
    """
    Business logic for creating a ticket.
    """
    return {
        "id": 1,
        "status": "open",
        "owner": user,
        "question": data["question"]
    }
