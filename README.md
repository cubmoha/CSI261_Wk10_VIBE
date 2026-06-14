# CSI261_Wk10_VIBE

## Student Records Management System

A comprehensive Python program that manages student records with three test scores, calculates grades, and provides advanced statistics and persistence features.

### Student Data Structure

Each student record contains:
- **Student Name** (string): Full name of the student
- **Student ID** (string): Unique identifier for the student
- **Test 1** (float): Score from the first test (0-100)
- **Test 2** (float): Score from the second test (0-100)
- **Test 3** (float): Score from the third test (0-100)
- **Calculated Average Score** (float): Mean of the three test scores
- **Calculated Letter Grade** (string): Based on the average score

### Grade Scale

- **A**: 90-100
- **B**: 80-89
- **C**: 70-79
- **D**: 60-69
- **F**: Below 60

## Key Improvements

### Code Organization
- **Modular Functions**: Code is organized into helper functions for better maintainability
  - `add_multiple_students()`: Handle adding multiple students in one session
  - `view_student_record()`: Display specific student information
  - `search_students()`: Search functionality
  - `main()`: Main program loop

### Error Handling
- **File Operations**: Robust error handling with try-except blocks for file I/O
- **Input Validation**: Validates all user inputs before processing
- **Error Messages**: Clear, informative error messages with ✗ indicators
- **KeyboardInterrupt**: Graceful handling of Ctrl+C interrupts

### User Experience
- **Clear Messages**: Status indicators (✓ for success, ✗ for errors)
- **Formatted Output**: All scores displayed to 2 decimal places
- **Multiple Entry**: Add multiple students in one session without returning to menu
- **Helpful Prompts**: Intuitive prompts guide users through operations

### Data Formatting
- **Consistent Precision**: All test scores and averages formatted to 2 decimal places
- **Pipe-Delimited Format**: Easy-to-read pipe-delimited file format
- **Header Row**: File includes header row for clarity

### Feature List

- ✅ **Add Multiple Students**: Add several students in one session
- ✅ **Automatic Calculations**: Average and letter grade calculated automatically
- ✅ **View Records**: Display individual student's information
- ✅ **Search Students**: Find students by name (case-insensitive)
- ✅ **View All Students**: Display summary table of all students with 2 decimal formatting
- ✅ **Class Statistics**: View highest average, lowest average, and class average
- ✅ **File Persistence**: Automatically saves and loads records from `student_grades.txt`
- ✅ **Error Handling**: Robust error handling for file operations and user input
- ✅ **Ctrl+C Support**: Gracefully exit using Ctrl+C keyboard interrupt

### Usage

Run the program:
```bash
python VIBE.py
```

### Feature List

- ✅ **Add Multiple Students**: Add several students in one session
- ✅ **Automatic Calculations**: Average and letter grade calculated automatically
- ✅ **View Records**: Display individual student's information
- ✅ **Search Students**: Find students by name (case-insensitive)
- ✅ **View All Students**: Display summary table of all students with 2 decimal formatting
- ✅ **Class Statistics**: View highest average, lowest average, and class average
- ✅ **File Persistence**: Automatically saves and loads records from `student_grades.txt`
- ✅ **Error Handling**: Robust error handling for file operations and user input
- ✅ **Ctrl+C Support**: Gracefully exit using Ctrl+C keyboard interrupt

### Menu Options

1. **Add a new student** - Enter student name, ID, and all three test scores. Can add multiple students without returning to menu.
2. **View student record (by ID)** - Display a specific student's complete information with scores to 2 decimal places
3. **Search student by name** - Find students by name (case-insensitive, partial match supported)
4. **View all students** - Display summary table of all students with formatted scores
5. **View class statistics** - Display class average, highest average, and lowest average
6. **Exit** - Close the program and save all changes (Ctrl+C also works)

### Functions

#### Helper Functions (Organized Code)
- **add_multiple_students()**: Allows adding multiple students in one session
- **view_student_record()**: Displays a specific student's information
- **search_students()**: Search for students by name
- **display_menu()**: Shows main menu options

#### Classes

##### Student
Represents an individual student with attributes:
- **Attributes**: name, id, test_1, test_2, test_3, average, grade
- **Methods**: 
  - add_test_1(), add_test_2(), add_test_3(): Add individual test scores (0-100)
  - _update_average_and_grade(): Auto-calculate average and grade
  - _calculate_grade(): Determine letter grade from average
  - all_scores_entered(): Check if all three scores are present
  - display_info(): Show detailed student information with formatted scores

##### StudentRecordManager
Manages the collection of students:
- **load_from_file()**: Load records from student_grades.txt (with error handling)
- **save_to_file()**: Save records to student_grades.txt (with error handling)
- **add_student()**: Add new student with validation
- **display_student()**: View individual student information
- **search_by_name()**: Find students by name (case-insensitive)
- **display_all_students()**: View all students in table format (2 decimal places)
- **calculate_class_statistics()**: Show class statistics

### File Format

Records are stored in `student_grades.txt` in pipe-delimited format for easy parsing:
```
name|id|test1|test2|test3|average|grade
John Smith|S001|85.0|90.0|88.0|87.67|B
Jane Doe|S002|92.0|95.0|88.0|91.67|A
```

### Example Usage

```
1. Add student "John Smith" with ID "S001"
2. Enter scores: Test 1=85, Test 2=90, Test 3=88
3. View record to see:
   - Test 1: 85, Test 2: 90, Test 3: 88
   - Average Score: 87.67
   - Letter Grade: B
4. Search for "John" to find the student
5. View all students to see class summary
6. Check class statistics for highest/lowest performers
7. Exit saves all changes to student_grades.txt
8. Next run automatically loads all saved records
```

### Data Persistence

- Student records are **automatically saved** when you add a new student
- Records are **automatically loaded** when the program starts
- All changes are persistent across program runs
- The file `student_grades.txt` is created in the same directory as the program
