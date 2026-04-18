from .all_patients import CREATE_ALL_PATIENTS
from .alk_fusion import CREATE_ALK_FUSION
from .ros1_fusion import CREATE_ROS1_FUSION
from .egfr_mutation import CREATE_EGFR_MUTATION
from .wt import CREATE_WT
from .treatments import CREATE_TREATMENTS
from .outcomes import CREATE_OUTCOMES

ALL_SCHEMAS = [
    CREATE_ALL_PATIENTS, CREATE_ALK_FUSION, CREATE_ROS1_FUSION,
    CREATE_EGFR_MUTATION, CREATE_WT, CREATE_TREATMENTS, CREATE_OUTCOMES
]
