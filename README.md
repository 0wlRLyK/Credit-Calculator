# Credit-Calculator {Hyperskill}  
Run the calculator:  
``` python creditcalc.py --type={{type}} ...```
## Parameters:
`--type` indicates the type of payment: "annuity" or "diff" (differentiated)  
`--payment` refers to the monthly payment of annuity  
`--principal` used for calculating of both types of payment  
`--periods` parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment, and the principal  
`--interest` used in differentiated mode; specified without the percentage sign
## Examples of use:
```python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6```  
Find loan principal and overpayment 
``` >> Your credit principal = 800018!  ```  
``` >> Overpayment = 246622  ```

```python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8```  
Find the number of years to repay the loan principal and overpayment  
``` >> You need 2 years to repay this credit!  ```  
``` >> Overpayment = 52000 ```


```python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10```  
Сalculate payments for 10 months
