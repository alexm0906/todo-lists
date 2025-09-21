select * from todo_profile;

update todo_profile set description = '<script>alert(1)</script>' where username = 'example';