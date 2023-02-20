# Ai-for-4bit-inputs-from-scratch
flashback to 2021 when i made neural network for 4bit inputs from scratch


this projec wast test if i could use my knowlage about neural nets and training algorythms to make the simplest neural network and train it



the idea :
make neural net that detects logic in examples and repeats it:

these are the training data:
![Screenshot 2023-02-20 121122](https://user-images.githubusercontent.com/61479273/220089596-208ba9d8-959b-4861-9d91-23fc67eb26af.png)

for 4 bit inputs we have total of 16 possible states
curently we are training on dataset with size of 8

this is our structure of the network:
![images](https://user-images.githubusercontent.com/61479273/220088950-05bb43ae-1cf3-44c2-86e9-b807e1793d1b.png)


firs we will make random weights and bias:
![Screenshot 2023-02-20 123530](https://user-images.githubusercontent.com/61479273/220095438-8b1b5478-50e2-40e0-90b0-5348ed238cbd.png)

then we train our network by adjusting our weights and bias by smaller and smaller amounts based on number of epochs and our learning rate:
![Screenshot 2023-02-20 130025](https://user-images.githubusercontent.com/61479273/220100600-0ed406f8-555b-4d66-95a2-a3ea0b9f5544.png)
![Screenshot 2023-02-20 130126](https://user-images.githubusercontent.com/61479273/220100818-6d0df288-836e-4b64-aa6f-2863e92f88a6.png)
![Screenshot 2023-02-20 1319252](https://user-images.githubusercontent.com/61479273/220105343-128a619d-3a9e-4f87-b9c3-e8b28f9df185.png)


and then we chose weights and biases that are better by good gueseses and error:
![Screenshot 2023-02-20 132143](https://user-images.githubusercontent.com/61479273/220106069-2e1e3827-704e-4b80-805b-d1b8e9e19724.png)
![Screenshot 2023-02-20 132304](https://user-images.githubusercontent.com/61479273/220106357-d977992e-7a0d-48ac-afb3-d1c5f0c68c30.png)


at the end we graph it and do lil demo for testing:
![Screenshot 2023-02-20 132304](https://user-images.githubusercontent.com/61479273/220112294-888f57dd-a3f6-4855-84d9-d3c566bf506e.png)

