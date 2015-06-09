'''
Abritrary tree class. Each tree has a root label two child nodes, which
should be other Trees or None.
>>> t = Tree(1, None, None)
[1, [2, [4, None, None], [5, None, None]], [3, None, [6, None, None]]]
>>> print t
[1, None, None]
>>> s = t.to_list()
>>> print s
[1, None, None]
>>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, None, Tree(6)))
>>> s = t.to_list()
>>> print s
[1, [2, [4, None, None], [5, None, None]], [3, None, [6, None, None]]]
>>> t2 = Tree.from_list(s)
>>> print t2
[1, [2, [4, None, None], [5, None, None]], [3, None, [6, None, None]]]
'''


class Tree(object):

    def __init__(self, label=None, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def to_list(self):
        '''
        Recursively build list representation of Tree. Each Tree is represented
        as [label, left, right], where left and right may themselves be list
        representation of child Trees.
        '''
        list = [self.label,
                self.left.to_list() if self.left else None,
                self.right.to_list() if self.right else None]

        return list

    def __repr__(self):
        return str(self.to_list())

    @classmethod
    def from_list(cls, lst):
        '''
        Create Tree from list represention of format [label, left, right],
        where left and right may themselves be list representations of child
        Trees. This format is the output of to_list().
        '''
        label = lst[0]

        if lst[1] is None:
            left = None
        else:
            left = cls.from_list(lst[1])

        if lst[2] is None:
            right = None
        else:
            right = cls.from_list(lst[2])

        return cls(label, left, right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
