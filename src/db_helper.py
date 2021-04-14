import mysql.connector


class DbHelper:
    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='employees')

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        QUERY = "SELECT MAX(salary) FROM salaries;"
        cur = self.conn.cursor(raw=True)
        cur.execute(QUERY)
        return int(cur.fetchone()[0])

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        QUERY = "SELECT MIN(salary) FROM salaries;"
        cur = self.conn.cursor(raw=True)
        cur.execute(QUERY)
        return int(cur.fetchone()[0])


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
