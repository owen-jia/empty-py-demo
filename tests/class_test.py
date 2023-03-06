from src.company.Company import Company
from src.company.Employee import Employee

cc = Company(name="Baidu", address="华夏中路", count=7000)
ee = Employee("杨小二")

cc.info()
try:
    ee.info()
except Exception as exc:
    print("Exception:", exc)
finally:
    print("finally")
