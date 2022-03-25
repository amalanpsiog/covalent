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

import json
import logging
from typing import Any, Optional, Sequence

import cloudpickle as pickle
from app.core.api import DataService
from app.schemas.results import Result
from fastapi import APIRouter, HTTPException

from covalent_dispatcher._db.dispatchdb import encode_result

router = APIRouter()


@router.get("/{dispatch_id}", status_code=200, response_model=Any)
async def fetch_result(*, dispatch_id: str) -> Any:
    """
    API Endpoint (/api/results/{dispatch_id}) to fetch result object
    """

    try:

        data = DataService()

        result_pkl_bytes = await data.get_result(dispatch_id)
        result = pickle.loads(result_pkl_bytes)
        return json.loads(encode_result(result))

    except Exception as err:
        error_message = "Error fetching result object"
        logging.exception(error_message)
        raise HTTPException(status_code=400, detail=error_message) from err