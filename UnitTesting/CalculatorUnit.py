#!/usr/bin/env python3

import unittest
import Calculator

class TestCalculatorMethods(unittest.TestCase):

  def test_add(self):
    self.assertEqual(Calculator.add(2,2),4)
    self.assertEqual(Calculator.add(-2,-2),-4)
    self.assertEqual(Calculator.add(2,-2),0)
    self.assertEqual(Calculator.add(2.2,2.2),4.4)
    try:
      result = Calculator.add("string1","string2")
    except:
      Exception
      pass
    else:
      self.fail('add() accepts strings as input')
    
  def test_subtract(self):
    self.assertEqual(Calculator.subtract(2,2),0)
    self.assertEqual(Calculator.subtract(-2,-2),0)
    self.assertEqual(Calculator.subtract(2,-2),4)
    self.assertEqual(Calculator.subtract(2.2,2.2),0)
    try:
      result = Calculator.subtract("string1","string2")
    except:
      Exception
      pass
    else:
      self.fail('subtract() accepts strings as input')
    
  def test_multiply(self):
    self.assertEqual(Calculator.multiply(2,2),4)
    self.assertEqual(Calculator.multiply(-2,-2),4)
    self.assertEqual(Calculator.multiply(2,-2),-4)
    
    
  def test_divide(self):
    self.assertEqual(Calculator.divide(2,2),1)
    self.assertEqual(Calculator.divide(-2,-2),1)
    self.assertEqual(Calculator.divide(2.0,2.0),1.0)
    self.assertEqual(Calculator.divide(2.20,2.2),1)
    self.assertRaises(ZeroDivisionError, Calculator.divide, 1, 0)
    
if __name__ == '__main__':
    unittest.main()
