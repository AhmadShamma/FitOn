from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsAuthenticatedAndOwner(BasePermission):
    
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == view.get_object().user.id

        # if request.method in ['GET','POST','PUT','PATCH','OPTIONS','HEAD']:
        #     return request.user.id == view.get_object().user.id
        # else:
        #     return False
        

# Define your custom permission class
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'retrieve':
            return True
        elif view.action in ['create', 'update', 'partial_update']:
            return request.user.is_authenticated
        return True
