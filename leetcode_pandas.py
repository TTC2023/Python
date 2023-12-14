import pd from pandas

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)