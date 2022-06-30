"""
When you are not sure how many parameters need to be declared during function definition,
use arbitrary number of arguments, *parameters
arbitrary arguments always take into tuple *
** : key value pair arbitrary number of arguments
*args, **kwargs
"""


def pizza(*topping):
    """ To add pizza topping """
    print(topping)


def library(**book):
    print(book)
    for title , author in book.items():
        print(title,author)


if __name__=='__main__':
    pizza('chilly')
    pizza('chilly','cheese','sweet corn','mashroom','paneer')
    library(title1='Hands  on machine learning with scikit-learn',author1='Aurelien geron',
    title2='Python for data analysis',author2='wes mckiney')
