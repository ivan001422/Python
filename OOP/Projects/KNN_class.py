'''
Датасет: 
sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
4.6,3.1,1.5,0.2,setosa
5,3.6,1.4,0.2,setosa
5.4,3.9,1.7,0.4,setosa
4.6,3.4,1.4,0.3,setosa
5,3.4,1.5,0.2,setosa
4.4,2.9,1.4,0.2,setosa
4.9,3.1,1.5,0.1,setosa
5.4,3.7,1.5,0.2,setosa
4.8,3.4,1.6,0.2,setosa
4.8,3,1.4,0.1,setosa
4.3,3,1.1,0.1,setosa
5.8,4,1.2,0.2,setosa
5.7,4.4,1.5,0.4,setosa
5.4,3.9,1.3,0.4,setosa
5.1,3.5,1.4,0.3,setosa
5.7,3.8,1.7,0.3,setosa
5.1,3.8,1.5,0.3,setosa
5.4,3.4,1.7,0.2,setosa
5.1,3.7,1.5,0.4,setosa
4.6,3.6,1,0.2,setosa
5.1,3.3,1.7,0.5,setosa
4.8,3.4,1.9,0.2,setosa
5,3,1.6,0.2,setosa
5,3.4,1.6,0.4,setosa
5.2,3.5,1.5,0.2,setosa
5.2,3.4,1.4,0.2,setosa
4.7,3.2,1.6,0.2,setosa
4.8,3.1,1.6,0.2,setosa
5.4,3.4,1.5,0.4,setosa
5.2,4.1,1.5,0.1,setosa
5.5,4.2,1.4,0.2,setosa
4.9,3.1,1.5,0.1,setosa
5,3.2,1.2,0.2,setosa
5.5,3.5,1.3,0.2,setosa
4.9,3.1,1.5,0.1,setosa
4.4,3,1.3,0.2,setosa
5.1,3.4,1.5,0.2,setosa
5,3.5,1.3,0.3,setosa
4.5,2.3,1.3,0.3,setosa
4.4,3.2,1.3,0.2,setosa
5,3.5,1.6,0.6,setosa
5.1,3.8,1.9,0.4,setosa
4.8,3,1.4,0.3,setosa
5.1,3.8,1.6,0.2,setosa
4.6,3.2,1.4,0.2,setosa
5.3,3.7,1.5,0.2,setosa
5,3.3,1.4,0.2,setosa
7,3.2,4.7,1.4,versicolor
6.4,3.2,4.5,1.5,versicolor
6.9,3.1,4.9,1.5,versicolor
5.5,2.3,4,1.3,versicolor
6.5,2.8,4.6,1.5,versicolor
5.7,2.8,4.5,1.3,versicolor
6.3,3.3,4.7,1.6,versicolor
4.9,2.4,3.3,1,versicolor
6.6,2.9,4.6,1.3,versicolor
5.2,2.7,3.9,1.4,versicolor
5,2,3.5,1,versicolor
5.9,3,4.2,1.5,versicolor
6,2.2,4,1,versicolor
6.1,2.9,4.7,1.4,versicolor
5.6,2.9,3.6,1.3,versicolor
6.7,3.1,4.4,1.4,versicolor
5.6,3,4.5,1.5,versicolor
5.8,2.7,4.1,1,versicolor
6.2,2.2,4.5,1.5,versicolor
5.6,2.5,3.9,1.1,versicolor
5.9,3.2,4.8,1.8,versicolor
6.1,2.8,4,1.3,versicolor
6.3,2.5,4.9,1.5,versicolor
6.1,2.8,4.7,1.2,versicolor
6.4,2.9,4.3,1.3,versicolor
6.6,3,4.4,1.4,versicolor
6.8,2.8,4.8,1.4,versicolor
6.7,3,5,1.7,versicolor
6,2.9,4.5,1.5,versicolor
5.7,2.6,3.5,1,versicolor
5.5,2.4,3.8,1.1,versicolor
5.5,2.4,3.7,1,versicolor
5.8,2.7,3.9,1.2,versicolor
6,2.7,5.1,1.6,versicolor
5.4,3,4.5,1.5,versicolor
6,3.4,4.5,1.6,versicolor
6.7,3.1,4.7,1.5,versicolor
6.3,2.3,4.4,1.3,versicolor
5.6,3,4.1,1.3,versicolor
5.5,2.5,4,1.3,versicolor
5.5,2.6,4.4,1.2,versicolor
6.1,3,4.6,1.4,versicolor
5.8,2.6,4,1.2,versicolor
5,2.3,3.3,1,versicolor
5.6,2.7,4.2,1.3,versicolor
5.7,3,4.2,1.2,versicolor
5.7,2.9,4.2,1.3,versicolor
6.2,2.9,4.3,1.3,versicolor
5.1,2.5,3,1.1,versicolor
5.7,2.8,4.1,1.3,versicolor
6.3,3.3,6,2.5,virginica
5.8,2.7,5.1,1.9,virginica
7.1,3,5.9,2.1,virginica
6.3,2.9,5.6,1.8,virginica
6.5,3,5.8,2.2,virginica
7.6,3,6.6,2.1,virginica
4.9,2.5,4.5,1.7,virginica
7.3,2.9,6.3,1.8,virginica
6.7,2.5,5.8,1.8,virginica
7.2,3.6,6.1,2.5,virginica
6.5,3.2,5.1,2,virginica
6.4,2.7,5.3,1.9,virginica
6.8,3,5.5,2.1,virginica
5.7,2.5,5,2,virginica
5.8,2.8,5.1,2.4,virginica
6.4,3.2,5.3,2.3,virginica
6.5,3,5.5,1.8,virginica
7.7,3.8,6.7,2.2,virginica
7.7,2.6,6.9,2.3,virginica
6,2.2,5,1.5,virginica
6.9,3.2,5.7,2.3,virginica
5.6,2.8,4.9,2,virginica
7.7,2.8,6.7,2,virginica
6.3,2.7,4.9,1.8,virginica
6.7,3.3,5.7,2.1,virginica
7.2,3.2,6,1.8,virginica
6.2,2.8,4.8,1.8,virginica
6.1,3,4.9,1.8,virginica
6.4,2.8,5.6,2.1,virginica
7.2,3,5.8,1.6,virginica
7.4,2.8,6.1,1.9,virginica
7.9,3.8,6.4,2,virginica
6.4,2.8,5.6,2.2,virginica
6.3,2.8,5.1,1.5,virginica
6.1,2.6,5.6,1.4,virginica
7.7,3,6.1,2.3,virginica
6.3,3.4,5.6,2.4,virginica
6.4,3.1,5.5,1.8,virginica
6,3,4.8,1.8,virginica
6.9,3.1,5.4,2.1,virginica
6.7,3.1,5.6,2.4,virginica
6.9,3.1,5.1,2.3,virginica
5.8,2.7,5.1,1.9,virginica
6.8,3.2,5.9,2.3,virginica
6.7,3.3,5.7,2.5,virginica
6.7,3,5.2,2.3,virginica
6.3,2.5,5,1.9,virginica
6.5,3,5.2,2,virginica
6.2,3.4,5.4,2.3,virginica
5.9,3,5.1,1.8,virginica
'''

class Sample:
    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            species=None
    ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification = None

    def classify(self, label: str) -> None:
        self.classification = label

    def matches(self) -> bool:  
        return self.classification == self.species


class Hyperparameter:
    def __init__(self, k: int, test_samples: list) -> None:
        self.k = k
        self.test_samples = test_samples
        self.quality = 0

    def test(self) -> None:
        correct = 0
        for sample in self.test_samples:
            guess = self.classify(sample)
            sample.classify(guess)
            correct += sample.matches()
        self.quality = correct / len(self.test_samples)

    def classify(self, sample: Sample) -> str:
        # Заглушка
        return 'virginica'


class Training_Data:
    def __init__(self, name: str) -> None:
        self.name = name
        self.training = []
        self.test = []
        self.tuning = []

    def load(self, path: str) -> None:
        file = open(path)
        file.readline()
        cnt = 0
        for line in file:
            cnt += 1
            parts = line.split(',')
            sepal_length = float(parts[0])
            sepal_width = float(parts[1])
            petal_length = float(parts[2])
            petal_width = float(parts[3])
            species = parts[4].strip()   # очистка от пробелов и \n
            sample = Sample(sepal_length, sepal_width, petal_length, petal_width, species)
            if cnt % 4 == 0:
                self.test.append(sample)
            else:
                self.training.append(sample)

    def testing(self, hyperparameter: Hyperparameter) -> None:
        hyperparameter.test()
        self.tuning.append(hyperparameter)


# ---------- Использование ----------
data = Training_Data('Data')
data.load('.venv/Data')

print(f"Обучающих: {len(data.training)}")
print(f"Тестовых: {len(data.test)}")

# Посмотрим, какие виды есть в тесте
print("Виды в тесте:", set(s.species for s in data.test))

hp1 = Hyperparameter(k=3, test_samples=data.test)
data.testing(hp1)

print(f"k={data.tuning[0].k}, quality={data.tuning[0].quality:.2%}")
