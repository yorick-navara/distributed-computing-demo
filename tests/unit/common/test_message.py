from uuid import uuid4
from datetime import datetime
import json

from common.message import Message

def test_serialize_deserialize():
    msg = Message(
        run_id=uuid4(),
        task_id=uuid4(),
        selections=[1,2,3],
        start_date = datetime.strptime('2022-11-01 00:00', '%Y-%m-%d %H:%M'),
        end_date = datetime.strptime('2022-12-01 00:00', '%Y-%m-%d %H:%M')
    )
    
    msg_str = msg.to_json()
    
    assert isinstance(msg_str, str)
    # assert valid JSON:
    try:
        json.loads(msg_str)
    except:
        assert False
    
    msg_deser = Message.from_json(msg_str)
    
    assert isinstance(msg_deser, Message)
    assert msg == msg_deser