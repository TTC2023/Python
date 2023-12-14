import pd from pandas

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    rows = employees.head(3)
    return rows

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id == 101][["name","age"]]

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees