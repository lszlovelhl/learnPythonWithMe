# permission_verification_decorator
def permission_required(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Simulate permission check
            if not hasattr(wrapper, 'has_permission'):
                print(f"Permission required: {permission}")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@permission_required("read")
def read_data():
    return "Data read successfully"

@permission_required("write")
def write_data():
    return "Data written successfully"

# Simulate setting permissions
read_data.has_permission = True  # Grant read permission
# Test the decorated functions
if __name__ == "__main__":
    print(read_data())  # Should succeed
    print(write_data())  # Should fail due to missing permission