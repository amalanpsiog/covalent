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

"""Unit tests for utils module"""


def test_is_empty():
    """Test that the MPQ contains only one element at any time."""
    pass


def preprocess_transport_graph():
    """Test that the execution status of the task nodes in the transport graph are initialized
    properly."""

    pass


def _post_process():
    """Test that lattice is post-processed correctly after execution of the nodes in the transport graph"""

    pass


def get_task_inputs():
    """
    Test that inputs for a given task execution are properly returned and parent nodes are passed
    as inputs to child nodes
    """
    pass


def test_is_sublattice():
    """Test sublattice check on a transport graph node"""

    pass


def test_are_tasks_running():
    """Test for status checks on running tasks"""
    pass


def test_get_task_order():
    """Test to check that task_order returns a non-empty list"""
    pass


def test_send_task_list_to_runner():
    """Test for sending task list to runner"""
    pass


def test_send_result_object_to_result_service():
    """Test for sending result object to result microservice."""
    pass


def test_send_task_update_to_result_service():
    """Test for sending task update to result service"""
    pass


def test_send_task_update_to_ui():
    """Test for sending task update to ui backend microservice."""
    pass


def test_get_result_object_from_result_service():
    """Test result object pickling from the result microservice"""
    pass


def test_update_result_and_ui():
    """Test that the UI is updated and the result is written to the database"""

    pass


def test_send_cancel_task_to_runner():
    """
    Test that the task to be cancelled by the runner returns a non-empty tuple containing the cancelled dispatch
    id and task id
    """

    pass


def test_is_sublattice_dispatch_id():
    """Test for sublattice dispatch id"""


def test_send_task_update_to_dispatcher():
    """Test for sending task update to dispatcher"""
    pass


def test_generate_task_result():
    """Test for generating task result"""
    pass
