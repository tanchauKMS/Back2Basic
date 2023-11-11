# Dry run

## Definition
- A dry run (or practice run) is a software testing process used to make sure that a system works correctly and will not result in severe failure.

-  For example, rsync, a utility for transferring and synchronizing data between networked computers or storage drives, has a "dry-run" option users can use to check that their command-line arguments are valid and to simulate what would happen when actually copying the data.


## Etymology (Fun Fact)
- The term dry run appears to have originated from fire departments in the US. In order to practice, they would carry out dispatches of the fire brigade where water was not pumped. 
- A run with real fire and water was referred to as a wet run. The more general usage of the term seems to have arisen from widespread use by the United States Armed Forces during World War II.

## Example with Python

```python
class DataRepository:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run

    def create_data(self, data):
        if self.dry_run:
            print("Dry run: Creating data:", data)
        else:
            # Logic to actually create data in the repository
            print("Creating data:", data)

    def update_data(self, data):
        if self.dry_run:
            print("Dry run: Updating data:", data)
        else:
            # Logic to actually update data in the repository
            print("Updating data:", data)

    def delete_data(self, data_id):
        if self.dry_run:
            print("Dry run: Deleting data with ID:", data_id)
        else:
            # Logic to actually delete data from the repository
            print("Deleting data with ID:", data_id)
```

- In the above example, the DataRepository class has a dry_run parameter in its constructor, which defaults to False. This parameter determines whether the repository operates in dry run mode or not.

- The create_data, update_data, and delete_data methods in the repository check the dry_run flag. If it is True, they print a message indicating that it is a dry run and show the intended operation without actually modifying the data. Otherwise, they execute the actual logic to create, update, or delete the data.

Here's how you can use the DataRepository class with and without the dry run mode:

```python
# Create a data repository instance without dry run mode
repo = DataRepository()
repo.create_data("New data")  # Output: Creating data: New data

# Create a data repository instance with dry run mode
dry_run_repo = DataRepository(dry_run=True)
dry_run_repo.create_data("New data")  # Output: Dry run: Creating data: New data
```