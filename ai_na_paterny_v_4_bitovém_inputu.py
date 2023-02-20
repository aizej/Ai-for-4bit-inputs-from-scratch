import time
import random
import matplotlib.pyplot as plt



learning_speed = 0.5            #float(input("zadejte learning speed 0 až 1 (0.99 je dobrý): "))
epochs = 20        #int(input("jaký chcete počet epoch?: "))



test = [
 [0, 0, 0, 1], 
 [0, 1, 0, 1], 
 [1, 1, 0, 1], 
 [0, 1, 1, 0], 
 [1, 1, 1, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [1, 0, 1, 1],
]

results = [
    0, 
    0, 
    0, 
    1, 
    1, 
    0, 
    0, 
    0,
]






weights = [(random.random() * 2 - 1), (random.random() * 2 - 1), (random.random() * 2 - 1), (random.random() * 2 - 1)]
bias = (random.random() * 2 - 1)

def AI(weights, inputs_numbers, bias):
    output = sum((inputs_numbers[i] * weights[i]) for i in range(len(inputs_numbers)))
    return (1 -(1/(1 + (2.71828182846 ** (output + bias))))) #sigmoid



def how_many_predicted(weights, bias):
    predictions = []

    for i in test:
        predictions.append(int(round(AI(inputs_numbers = i, weights = weights, bias=bias), 0)))


    predicted_correctly = 0
    a = 0
    for i in predictions:
        if i == results[a]:
            predicted_correctly += 1
        a += 1

    return (predicted_correctly/len(results))


def get_error(weights, bias):
    results_after_training = []

    for i in test:
        results_after_training.append(AI(inputs_numbers = i, weights = weights,bias=bias))
        
    
    error_of_all = 0
    for i in results_after_training:
        error_of_all += ((i - results[ results_after_training.index(i) ] ) ** 2)

    return  (error_of_all/len(results))


to_plot = []
def train(epochs):
    global weights
    global bias
    global cislo_na_nasobeni_a_deleni
    for i in range(epochs):
        to_plot.append(get_error(weights,bias))
        cislo_na_nasobeni_a_deleni = (1 / ((i + 1) ** (learning_speed**0.5)))

        print (f"Epocha {(i + 1)}:")
        print(how_many_predicted(weights,bias))
        

        #decreases or increrases every weight and saves what is better
        for i in weights:                           
            better_weights = list(weights)
            better_weight = (i + cislo_na_nasobeni_a_deleni)
            better_weights[weights.index(i)] = better_weight 

            if (how_many_predicted(better_weights,bias) > how_many_predicted(weights,bias)) or ((get_error(better_weights,bias)) < (get_error(weights,bias)) and (how_many_predicted(better_weights,bias) >= how_many_predicted(weights,bias))): #((get_error(better_weights)) < (get_error(weights)))
                i = better_weight
                weights = list(better_weights)
        

            better_weights = list(weights)
            better_weight = (i - cislo_na_nasobeni_a_deleni)
            better_weights[weights.index(i)] = better_weight


            if (how_many_predicted(better_weights,bias) > how_many_predicted(weights,bias)) or ((get_error(better_weights,bias)) < (get_error(weights,bias)) and (how_many_predicted(better_weights,bias) >= how_many_predicted(weights,bias))): #((get_error(better_weights)) < (get_error(weights)))
                weights = list(better_weights)


        #same as with weights but with bias
        better_bias = (bias + cislo_na_nasobeni_a_deleni)

        if (how_many_predicted(weights,better_bias) > how_many_predicted(weights,bias)) or ((get_error(weights,better_bias)) < (get_error(weights,bias)) and (how_many_predicted(weights,better_bias) >= how_many_predicted(weights,bias))): #((get_error(better_weights)) < (get_error(weights)))
            bias = better_bias

        better_bias = (bias - cislo_na_nasobeni_a_deleni)

        if (how_many_predicted(weights,better_bias) > how_many_predicted(weights,bias)) or ((get_error(weights,better_bias)) < (get_error(weights,bias)) and (how_many_predicted(weights,better_bias) >= how_many_predicted(weights,bias))): #((get_error(better_weights)) < (get_error(weights)))
            bias = better_bias










to_plot.append(get_error(weights,bias))
train(epochs)

plt.plot(to_plot)
print(cislo_na_nasobeni_a_deleni)
print(weights)
print(bias)
print(get_error(weights,bias))
plt.show()
print("training done!")


def test_ai():
    while True:
        cislo_jedna = float(input("zadejte hodnotu:"))
        cislo_dva = float(input("zadejte hodnotu:"))
        cislo_tri = float(input("zadejte hodnotu:"))
        cislo_4 = float(input("zadejte hodnotu:"))
        users_input_numbers = [cislo_jedna, cislo_dva, cislo_tri, cislo_4]
        if(AI(weights = weights, bias=bias, inputs_numbers = users_input_numbers)) >= 0.5:
            print(f"ano\npravděpodobnost:{((AI(weights = weights, bias=bias, inputs_numbers = users_input_numbers)) * 100)}%")
        else:
            print(f"ne\npravděpodobnost:{(1 - (AI(weights = weights, bias=bias, inputs_numbers = users_input_numbers))) * 100}%")


test_ai()