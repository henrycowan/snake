
class SnakeBody:


    def __init__(self, pos_i):
        self.body_length = 1
        self.body_pos = [(0,0)]
        self.pos_i = pos_i
        self.snake_to_plot = []
        self.food_aquired = 1
        self.fail_condition = False
        self.update_snake(pos_i)
        self.delete_snake_pos = []

    def add_position(self, new_position_value):
        self.body_pos[self.body_length-1] = new_position_value

    def increase_body_length(self):
        self.body_length += 1
        self.body_pos.append([0,0])

    def check_fail(self, new_pos):
        if self.snake_to_plot.__contains__(new_pos):
            self.fail_condition = True

    def update_snake(self, new_pos):

        self.increase_body_length()
        self.check_fail(new_pos)
        self.add_position(new_pos)
        self.cut_snake()

    def cut_snake(self):
        self.snake_to_plot = self.body_pos[self.body_length-self.food_aquired:self.body_length]
