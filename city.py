from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random

class build(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        pass  
    
class park(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        pass

class car(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        current_position = self.pos
        cellmates = self.model.grid.get_cell_list_contents([current_position])
        #for agent in cellmates:
         #   if isinstance(agent, build):
          #      print(f"Agente {self.unique_id} chocó con un edificio en la posición {current_position}")
          
        possible = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        while True:
            new_position = random.choice(possible)
            if self.model.grid.is_cell_empty(new_position):
                self.model.grid.move_agent(self, new_position)
                break
    
class cityModel(Model):
    def __init__(self, N, w, h):
        self.num_agents = N
        self.grid = MultiGrid(w, h, True)
        self.schedule = RandomActivation(self)
        
        # Crear y colocar agentes `car`
        for i in range(self.num_agents):
            a = car(i, self)
            self.schedule.add(a)
            while True:
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)
                if self.grid.is_cell_empty((x, y)):
                    self.grid.place_agent(a, (x, y))
                    break
        
        unique_id = self.num_agents
        
        # Crear y colocar agentes `build` y `park`
        for i in range(2, 12):
            for j in range(2, 4):
                if ((i == 9 and j == 2) or (i == 4 and j == 3)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(2, 12):
            for j in range(6, 8):
                if ((i == 3 and j == 6) or (i == 10 and j == 7)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(13, 15):
            for j in range(9, 11):
                b = build(unique_id, self)
                self.schedule.add(b)
                self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(2, 6):
            for j in range(12, 17):
                if ((i == 4 and j == 12) or (i == 2 and j == 15)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(2, 6):
            for j in range(19, 22):
                if ((i == 4 and j == 19)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(8, 12):
            for j in range(12, 22):
                if ((i == 10 and j == 12) or (i == 8 and j == 14) or (i == 11 and j == 17) or (i == 9 and j == 21)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
        
        for i in range(16, 18):
            for j in range(2, 4):
                b = build(unique_id, self)
                self.schedule.add(b)
                self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(20, 22):
            for j in range(2, 4):
                if (i == 21 and j == 3):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(16, 18):
            for j in range(6, 8):
                if (i == 17 and j == 6):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(20, 22):
            for j in range(6, 8):
                b = build(unique_id, self)
                self.schedule.add(b)
                self.grid.place_agent(b, (i, j))
                unique_id += 1
        
        for i in range(16, 22):
            for j in range(12, 16):
                if ((i == 18 and j == 12) or (i == 20 and j == 15)):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(16, 18):
            for j in range(18, 22):
                if (i == 17 and j == 21):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
                
        for i in range(20, 22):
            for j in range(18, 22):
                if (i == 20 and j == 18):
                    p = park(unique_id, self)
                    self.schedule.add(p)
                    self.grid.place_agent(p, (i, j))
                else:
                    b = build(unique_id, self)
                    self.schedule.add(b)
                    self.grid.place_agent(b, (i, j))
                unique_id += 1
    
    def step(self):
        self.schedule.step()