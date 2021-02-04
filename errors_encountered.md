## Error 1
PS C:\Users\mweny\Desktop\DPG assignment ufuk\DPG-assignment> .\my_env\Scripts\activate
.\my_env\Scripts\activate : File C:\Users\mweny\Desktop\DPG assignment ufuk\DPG-assignment\my_env\Scripts\activate.ps1 cannot be loaded because running scripts is    
disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\my_env\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

## Solution 1
PS C:\Users\mweny\Desktop\DPG assignment ufuk> Set-ExecutionPolicy -Scope CurrentUser

cmdlet Set-ExecutionPolicy at command pipeline position 1
Supply values for the following parameters:
ExecutionPolicy: unrestricted
PS C:\Users\mweny\Desktop\DPG assignment ufuk>

## Result 1
PS C:\Users\mweny\Desktop\DPG assignment ufuk\DPG-assignment> .\my_env\Scripts\activate
(my_env) PS C:\Users\mweny\Desktop\DPG assignment ufuk\DPG-assignment>