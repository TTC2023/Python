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

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    new_data = customers.drop_duplicates(subset='email')
    return new_data

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    df_filtered = pd.DataFrame(students)[students['name'].notnull()]
    return df_filtered

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
        }
    )
    return students

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students