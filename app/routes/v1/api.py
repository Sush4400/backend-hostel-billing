from fastapi import APIRouter

from app.routes.v1.endpoints.auth import router as auth_router
from app.routes.v1.endpoints.counter import router as counter_router
from app.routes.v1.endpoints.menus import router as menu_router
from app.routes.v1.endpoints.orders import router as order_router
from app.routes.v1.endpoints.payments import router as payment_router
from app.routes.v1.endpoints.print_jobs import router as print_job_router
from app.routes.v1.endpoints.reports import router as report_router



api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(counter_router)
api_router.include_router(menu_router)
api_router.include_router(order_router)
api_router.include_router(payment_router)
api_router.include_router(print_job_router)
api_router.include_router(report_router)