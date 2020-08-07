class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head
        # Constant Loop to find the correct node with the corresponding key you are looking for
        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):
        # check if the key is already in the linked list
            # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next

        # if we reach the end of the list, it's not here! 
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity 
        self.bucket = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.bucket)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5432
        byte_array = key.encode()
        for b in byte_array:
            hash = ((hash*33)^b) % 0x100000000
        return hash



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.bucket[index] == None:
            self.bucket[index] = HashTableEntry(index,value)
        else:
            self.bucket[LinkedList().update_or_else_insert_at_head(index,value)]


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # This probably doesn't work 
        # So I need to delete a value that could be in a linked list but i need to iterate through the list and find a base case where the key is equal to the key we are looking for
        index = self.hash_index(key)
        if (self.bucket[index] == key):
            self.bucket[index] = None
        else:
            #  Need to figure out how to make the delete function on the next node in the linked list
            return self.delete(LinkedList().find(key)) 



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if (self.bucket[index] == None):
            return
        else:
            entry = self.bucket[index].find(key)
            # if it's found entry will be the node
            if (entry != None):
                return entry.value
            else:
                return entry

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.       ​
        Implement this.
        """
        # Your code here
        # Change the capicity to the new capacity that is passed in
        # For every key in the in the Hashtable rehash it
        # self.bucket = [None] * new_capacity
        # store the old bucket

        temp_storage = self.bucket
        # create new bucket with the new capacity
        self.bucket = [None] * new_capacity
        self.capacity = new_capacity
        # we loop through temp_storage and put everything in our new bucket
        for ll in temp_storage:
            if ll is not None:
                cur = ll.head
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
