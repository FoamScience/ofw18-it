import os
import pytest
import oftest
from oftest import run_reset_case

def file_mod(nu):
    return {
        "constant/transportProperties":
        [
            ('nu',  f"{nu}")
        ]
    }
def meta_data(nu):
    return {"nu":nu, "script": "Allrun"}

dir_name = os.path.dirname(os.path.abspath(__file__))
params = [oftest.Case_modifiers(file_mod(nu), dir_name, meta_data(nu)) for nu in [1e-3, 1e-4, 1e-5]]

@pytest.mark.parametrize("run_reset_case",params, indirect=True)
def test_completed(run_reset_case):
    log = oftest.path_log()
    assert oftest.case_status(log) == 'completed'
