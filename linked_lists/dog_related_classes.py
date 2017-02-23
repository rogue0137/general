#!/usr/bin/python

class AryaTheDog(object):
    """ This class creates a dog """
    def __init__(self, description_value):
      self.description_value = description_value
      self.next = None



class AllAboutArya(object):
    """ This class creates a started list of dogs """
    def __init__(self, start=None):
      self.start = start
      

    def append(self, new_description):
        current_description = self.start
        if self.start:
            while current_description.next:
                current_description = current_description.next
            current_description.next = new_description
            #print('current_description.next: ' + str(new_description))
        else:
          self.start = new_description
          #print('self.start: ' + str(new_description))

    def get_dog_description_position(self,position_of_dog_description):
        description_counter = 1
        current_description = self.start
        if position_of_dog_description < 1:
            return None
        while current_description and description_counter <= position_of_dog_description:
            if description_counter == position_of_dog_description:
                return current_description
            current_description = current_description.next
            description_counter += 1
        return None
    
    def insert_new_description(self,new_description,position_of_dog_description):
        description_counter = 1
        current_description = self.start
        if position_of_dog_description > 1:
            while current_description and description_counter < position_of_dog_description:
                    if description_counter == position_of_dog_description - 1:
                        new_description.next = current_description.next
                        current_description.next = new_description
                    current_description = current_description.next
                    description_counter += 1
        elif position_of_dog_description == 1:
            new_description.next = self.start
            self.start = new_description
            
    def delete_old_description(self,description_value):      
        current_description = self.start
        previous_description = None
        while current_description.description_value != description_value and current_description.next:
            previous_description = current_description
            current_description = current_description.next 
        if current_description.description_value == description_value:
            if previous_description:
                previous_description.next == current_description.next
            else:
                self.start = current_description.next

