from collections import namedtuple


class TaggedDocument(namedtuple('TaggedDocument', 'words tags aaa')):

    def __str__(self):
        print(self._fields)
        """Human readable representation of the object's state, used for debugging.

        Returns
        -------
        str
           Human readable representation of the object's state (words and tags).

        """
        return '%s(%s, %s,"aaa")' % (self.__class__.__name__, self.words, self.tags)