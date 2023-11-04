{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "robert\n",
      "89\n",
      "92\n",
      "19\n",
      "200\n"
     ]
    }
   ],
   "source": [
    "from tools import Student\n",
    "\n",
    "stu1 = Student(name=\"robert\",chinese=89,english=92,math=19)\n",
    "print(stu1.name)\n",
    "print(stu1.chinese)\n",
    "print(stu1.english)\n",
    "print(stu1.math)\n",
    "print(stu1.sum())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
