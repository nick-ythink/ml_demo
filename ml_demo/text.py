text_eng = {
    'main_screen_text': ('Instructions:\n'
                         'Select a model from the menu to the right, enter or load data and experiment using the different '
                         'algorithms to train models and make predictions, or load an already trained model to start using it '
                         'to predict! If you need help click \'help\' at any time.'),
    'nn_help_text': ('Neural Networks are loosely based on a simplified model of the brain.\n\n'
                     'To train a NeuralNetwork load in correctly formatted data by pressing the "Load Training Data" button. '
                     'Once the data is loaded press the "Train" button and wait. You can leave the the Neural Network parameters '
                     'as their defaults or adjust them by adjusting the sliders. You can also view the training graph by clicking '
                     'the "Training Graph" button, this shows you how accurate the model was after each training iteration.\n\n'
                     'You can also save and load previously trained models using the corresponding buttons. When loaded you can '
                     'Make predictions using it.\n\n'
                     'To make predictions, load in correctly formatted data by clicking the "Load Predicting Data" button, then '
                     'press "Predict", the prediciton will appear on the screen.\n\n'
                     'The parameters: Lambda is regularisation strength, at the right strength there will be a good balance '
                     'between being accurate and its ability to be applied to new data. Controls how much the network gets '
                     'adjusted each training iteration. To low and it will take too long to train and too high and it will go '
                     'past the most accurate point and become less accurate again. Epochs is the maximum number of iterations '
                     'To take training the network. The network should exponentially get more accurate, after a while it\'s not '
                     'worth training any further, setting the epochs to this point is best. Adaptive and Decrease work together to '
                     'control how much the network gets adjusted with each training iteration as it gets more accurate. Hidden '
                     'Layer Size adjusts how many nodes are present in the hidden layer. The more of these there are the more '
                     'complex the resultant function is. If Train/Test is activated, you input data will be split into training '
                     'and testing data and your network\'s accuracy will be evaluated. This will be shown to you when it has been '
                     'trained.'),
    'dt_help_text': ('Decision Trees make predictions by making a decision at each node and passing the results to the following '
                     'child nodes. They are easy to interpret by humans, unlike Neural Networks.\n\n'
                     'To train a NeuralNetwork load in correctly formatted data by pressing the "Load Training Data" button. '
                     'Once the data is loaded press the "Train" button and wait.\n\n'
                     'You can also save and load previously trained models using the corresponding buttons. When loaded you can '
                     'Make predictions using it.\n\n'
                     'To make predictions, load in correctly formatted data by clicking the "Load Predicitng Data" button, then '
                     'press "Predict", the prediciton will appear on the screen.\n\n'),
}
