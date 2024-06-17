# %% [markdown]
# # Câu hỏi tự luận
# ## Câu 1

# %%
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self, data):
        super(Softmax, self).__init__()
        self.data = data

    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x), dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self, data):
        super(SoftmaxStable, self).__init__()
        self.data = data

    def forward(self, x):
        numerator = x - torch.max(x)
        return torch.exp(numerator) / torch.sum(torch.exp(numerator), dim=0)


data = torch.Tensor([1, 2, 300000000])

model = Softmax(data)
output = model(data)
print(output)

model = SoftmaxStable(data)
output = model(data)
print(output)

# %% [markdown]
# ## Câu 2

# %%
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self) -> None:
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        sum_value = 0
        count = 0
        for person in self.people:
            if isinstance(person, Teacher):
                sum_value += person.yob
                count += 1
        return sum_value / count

    def describe(self):
        print(f"Phường: {self.name}")
        print("Danh sách người:")
        for person in self.people:
            person.describe()


class Person:
    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"\tTên: {self.name}")


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name)
        self.yob = yob
        self.grade = grade

    def describe(self):

        super().describe()
        print(f"\t\tNăm sinh: {self.yob}")
        print(f"\t\tLớp: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name)
        self.yob = yob
        self.subject = subject

    def describe(self):
        super().describe()
        print(f"\t\tNăm sinh: {self.yob}")
        print(f"\t\tMôn giảng dạy: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name)
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        super().describe()
        print(f"\t\tNăm sinh: {self.yob}")
        print(f"\t\tChuyên môn: {self.specialist}")


# Tạo một Ward và thêm người vào
ward = Ward("Phường 1")
ward.add_person(Student("Huy", 2005, "12A1"))
ward.add_person(Teacher("Nam", 1970, "Văn"))
ward.add_person(Teacher("Lan", 1980, "Toán"))
ward.add_person(Doctor("Chu", 1990, "Nha"))
ward.add_person(Doctor("Hoa", 2000, "Da liễu"))


# In thông tin của mỗi người trong Ward
# ward.describe()

# Sắp xếp người theo tuổi
ward.sort_age()
ward.describe()

# In số lượng bác sĩ trong Ward
print(f"Số lượng bác sĩ trong Ward: {ward.count_doctor()}")

# Tính tuổi trung bình của giáo viên trong Ward
print(f"Tuổi trung bình của giáo viên trong Ward: {ward.compute_average()}")

# %% [markdown]
# ## Câu 3

# %%
class Stack:
    def __init__(self, capacity):
        # https://stackoverflow.com/a/311833
        # Dù có khởi tạo một danh sách rỗng trước cũng không tăng hiệu suất được bao nhiêu.
        self.capacity = capacity
        self.elements_list = []

    def is_empty(self):
        return len(self.elements_list) == 0
    
    def is_full(self):
        return len(self.elements_list) == self.capacity
    
    def pop(self):
        if self.is_empty():
            return None
        return self.elements_list.pop()
    
    def push(self, value):
        if self.is_full():
            return None
        self.elements_list.append(value)

    def top(self):
        if self.is_empty():
            return None
        return self.elements_list[-1]
    
stack = Stack(5)

stack.push(1)
stack.push(2)

print(stack.is_full())
print(stack.top())
print(stack.pop())
print(stack.top())
print(stack.pop())
print(stack.is_empty())

# %% [markdown]
# ## Câu 4

# %%
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements_list = []

    def is_empty(self):
        return len(self.elements_list) == 0
    
    def is_full(self):
        return len(self.elements_list) == self.capacity
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements_list.pop(0)
    
    def enqueue(self, value):
        if self.is_full():
            return None
        self.elements_list.append(value)

    def front(self):
        if self.is_empty():
            return None
        return self.elements_list[0]
    
queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)

print(queue.is_full())
print(queue.front())
print(queue.dequeue())
print(queue.front())
print(queue.dequeue())
print(queue.is_empty())

# %% [markdown]
# # Câu hỏi trắc nghiệm