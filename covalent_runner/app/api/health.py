# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.
from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter()


class HealthResponse(BaseModel):
    is_healthy: bool = True


class ReadyResponse(BaseModel):
    is_ready: bool = True


@health_router.get("/", status_code=200, response_model=HealthResponse)
@health_router.get("/healthz", status_code=200, response_model=HealthResponse)
def is_service_healthy():
    """
    This endpoint is intended to determine whether the application container is at a healthy state
    or failed to startup up hence needs to be restarted.
    """
    return {"is_healthy": True}


@health_router.get("/readyz", status_code=200, response_model=ReadyResponse)
def is_service_ready():
    """
    This endpoint is intended to determine whether the application is ready to accept requests from
    downstream services.
    """
    return {"is_ready": True}