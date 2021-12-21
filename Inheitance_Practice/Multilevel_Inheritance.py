class Grand_Parent:
    def __init__(self,grand_parent_name, age, alive):
        self.grand_parent_name = grand_parent_name
        self.age = age
        self.alive = alive

    def show_grand_parent_details(self):
        print(f"This is Grand Father :{self.grand_parent_name}")
        print(f"Grand Father age :{self.age}")
        print(f"Grand Father alive :{self.alive}")

class Parent(Grand_Parent):
    def __init__(self,grand_parent_name, age, alive,parent_name, parent_age):
        super().__init__(grand_parent_name, age, alive)
        self.parent_name = parent_name
        self.parent_age = parent_age

    def show_parent_details(self):
        print(f"This is Parent :{self.parent_name}")
        print(f"Parent age :{self.parent_age}")


class Child(Parent):
    def __init__(self,grand_parent_name, age, alive,parent_name, parent_age, child_name,child_age):
        super().__init__(grand_parent_name, age, alive,parent_name,parent_age)
        self.child_name = child_name
        self.child_age = child_age

    def show_child_details(self):
        print(f"This is child :{self.child_name}")
        print(f"Child age :{self.child_age}")

child1=Child(grand_parent_name="Ramchandra Havele",age=90, alive="No", parent_name="Mahesh Havele",parent_age=60,child_name="Ravindra Havele",child_age=36)
child1.show_grand_parent_details()
child1.show_parent_details()
child1.show_child_details()