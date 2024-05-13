from django.core.exceptions import ValidationError


# class CaseLetterValidator:
#     message = "Your password must contain lowercase letter."
#     message2 = "Your password must contain uppercase letter."
    
#     code = "passowrd_no_lowercase"
#     def validate(self, password, user=None):
#         if not any(char.islower() for char in password):
#             raise ValidationError(self.message, self.code, params={"password": password})
#         if not any(char.isupper() for char in password):
#             raise ValidationError(self.message2 , self.code,params={"pass":password})
        

#     def get_help_text(self):
#         return "Your password must contain lowercase letter."