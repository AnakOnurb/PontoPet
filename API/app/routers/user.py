from fastapi import APIRouter

router = APIRouter()

@router.get("/search", tags=["users"], summary="search users")
async def get_users():
    return {"users": []}

@router.get("/{user_id}", tags=["users"], summary="get user")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.put("/{user_id}", tags=["users"], summary="update user")
async def update_user(user_id: int, name: str, email: str, document: str, password: str, login: str):
    return {
        "updated":1,
        "user_id": user_id,
        "name": name,
        "email": email,
        "document": document,
        "password": password,
        "login": login
    }

@router.post("/create", tags=["users"], summary="create user")
async def create_user(name: str, email: str, document: str, password: str, login: str):
    return {
        "created":1,
        "name": name,
        "email": email,
        "document": document,
        "password": password,
        "login": login
    }

@router.put("{user_id}/role/assign", tags=["users"], summary="assign role to user")
async def update_user(user_id: int, role_id: int):
    return {
        "assigned":1,
        "user_id": user_id,
        "role_id": role_id
    }

@router.put("{user_id}/role/revoke", tags=["users"], summary="revoke role from user")
async def update_user(user_id: int, role_id: int):
    return {
        "updated":1,
        "revoked": user_id,
        "role_id": role_id
    }