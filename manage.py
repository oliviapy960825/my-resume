from flask_script import Manager
from starter import app, db, Professor, Course

manager = Manager(app)


@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    DragoneDebra = Professor(name='Dragone Debra', department='ACCT')
    DePueCynthia = Professor(name='DePue Cynthia', department='ACCT')
    AtlasJames = Professor(name='Atlas James', department='CISC')
    ACCT208 = Course(number=208,title='AccountingII', description='Introduction to managerial accounting', professor=DragoneDebra)
    ACCT352 = Course(number=352,title='Law and Social Issues in Business', description='Focuses on the legal environment of business, including objectives of the law, sources of the law, regulatory and judicial process, and effect of government and society on the formation and evolution of the law',professor=DePueCynthia)
    CISC181 = Course(number=181,title='Introduction to Computer Science II', description='Principles of computer science illustrated and applied through programming in an object oriented language. Programming projects illustrate computational problems, styles and issues that arise in computer systems development and in all application areas of computation',professor=AtlasJames)
    CISC220 = Course(number=220,title='Data Structures', description='Review of data type abstraction, recursion, arrays, stacks, queues, multiple stacks and linked lists. Emphasis on dynamic storage management, garbage collection, trees, graphs, tables, sorting and searching',professor=AtlasJames)
    db.session.add(DragoneDebra)
    db.session.add(DePueCynthia)
    db.session.add(AtlasJames)
    db.session.add(ACCT208)
    db.session.add(ACCT352)
    db.session.add(CISC181)
    db.session.add(CISC220)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
