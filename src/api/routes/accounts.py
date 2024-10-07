from fastapi import Depends
from fastapi.routing import APIRouter

from core.accounts.entities.dto import AccountReadDTO, AccountRegistryDTO
from src.core.accounts.services.accounts import AccountService

router = APIRouter(tags=["Accounts"])


@router.post("/")
async def create_account(
    accounts: AccountRegistryDTO,
    service: AccountService = Depends(AccountService),
) -> AccountReadDTO:
    result = await service.create(accounts)

    return AccountReadDTO.model_validate(result)
