class Dog(object):
    """ This class creates a dog """
    def __init__(self, value):
      self.value = value
      self.next = None



class LinkedDogs(object):
    """ This class creates a linked list of dogs """
    def __init__(self, link=None):
      self.link = link

    def append(self, new_dog):
        current = self.link
        if self.link:
            while current.next:
                current = current.next
            current.next = new_dog
        else:
          self.link = new_dog






