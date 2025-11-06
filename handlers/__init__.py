from .lang_handler import router as lang_router
from .company_handler import router as company_router
from .drug_handler import router as drug_router
from .user_handler import router as user_router
from .feedback_handler import router as feedback_router

__all__ = [
    'lang_router',
    'company_router',
    'drug_router',
    'user_router',
    'feedback_router'
]
