# Mohammed Mills
# CIS261
# VIBE CODING
# Student Records Management System

import os


class Student:
    """Represents a student with three test scores and grade calculation."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.test_1 = None
        self.test_2 = None
        self.test_3 = None
        self.average = None
        self.grade = None
    
    def add_test_1(self, score):
        """Add Test 1 score and update average and grade."""
        if 0 <= score <= 100:
            self.test_1 = score
            self._update_average_and_grade()
            return True
        return False
    
    def add_test_2(self, score):
        """Add Test 2 score and update average and grade."""
        if 0 <= score <= 100:
            self.test_2 = score
            self._update_average_and_grade()
            return True
        return False
    
    def add_test_3(self, score):
        """Add Test 3 score and update average and grade."""
        if 0 <= score <= 100:
            self.test_3 = score
            self._update_average_and_grade()
            return True
        return False
    
    def _update_average_and_grade(self):
        """Update average and grade based on current test scores."""
        if self.all_scores_entered():
            self.average = (self.test_1 + self.test_2 + self.test_3) / 3
            self._calculate_grade()
        else:
            self.average = None
            self.grade = None
    
    def _calculate_grade(self):
        """Calculate letter grade based on average score."""
        if self.average is None:
            self.grade = 'N/A'
        elif self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'
    
    def all_scores_entered(self):
        """Check if all three test scores have been entered."""
        return self.test_1 is not None and self.test_2 is not None and self.test_3 is not None
    
    def display_info(self):
        """Display student information and grades."""
        print(f"\n{'='*55}")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.id}")
        test1_str = f"{self.test_1:.2f}" if self.test_1 is not None else "Not entered"
        test2_str = f"{self.test_2:.2f}" if self.test_2 is not None else "Not entered"
        test3_str = f"{self.test_3:.2f}" if self.test_3 is not None else "Not entered"
        print(f"Test 1: {test1_str}")
        print(f"Test 2: {test2_str}")
        print(f"Test 3: {test3_str}")
        
        if self.all_scores_entered():
            print(f"Average Score: {self.average:.2f}")
            print(f"Letter Grade: {self.grade}")
        else:
            print(f"Average Score: Pending")
            print(f"Letter Grade: Pending")
        print(f"{'='*55}")


class StudentRecordManager:
    """Manages multiple student records."""
    
    def __init__(self):
        self.students = {}
        self.filename = "student_grades.txt"
    
    def load_from_file(self):
        """Load student records from file in pipe-delimited format with error handling."""
        if not os.path.exists(self.filename):
            return  # File doesn't exist yet, no records to load
        
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                if not lines:
                    return
                
                # Skip header if present
                start_idx = 1 if lines[0].startswith('name|') else 0
                loaded_count = 0
                
                for line in lines[start_idx:]:
                    line = line.strip()
                    if not line:
                        continue
                    
                    try:
                        parts = line.split('|')
                        if len(parts) >= 7:
                            student = Student(parts[0], parts[1])
                            student.test_1 = float(parts[2]) if parts[2] != 'None' else None
                            student.test_2 = float(parts[3]) if parts[3] != 'None' else None
                            student.test_3 = float(parts[4]) if parts[4] != 'None' else None
                            student.average = float(parts[5]) if parts[5] != 'None' else None
                            student.grade = parts[6] if parts[6] != 'None' else None
                            self.students[student.id] = student
                            loaded_count += 1
                    except (ValueError, IndexError):
                        # Skip malformed lines
                        continue
                
                if loaded_count > 0:
                    print(f"✓ Successfully loaded {loaded_count} student record(s) from {self.filename}\n")
        except IOError as e:
            print(f"✗ Error reading file {self.filename}: {e}\n")
        except Exception as e:
            print(f"✗ Unexpected error loading file: {e}\n")
    
    def save_to_file(self):
        """Save student records to file in pipe-delimited format with error handling."""
        try:
            with open(self.filename, 'w') as f:
                # Write header
                f.write("name|id|test1|test2|test3|average|grade\n")
                # Write student records
                for student in self.students.values():
                    test_1 = f"{student.test_1:.2f}" if student.test_1 is not None else "None"
                    test_2 = f"{student.test_2:.2f}" if student.test_2 is not None else "None"
                    test_3 = f"{student.test_3:.2f}" if student.test_3 is not None else "None"
                    average = f"{student.average:.2f}" if student.average is not None else "None"
                    grade = str(student.grade) if student.grade is not None else "None"
                    f.write(f"{student.name}|{student.id}|{test_1}|{test_2}|{test_3}|{average}|{grade}\n")
            return True
        except IOError as e:
            print(f"✗ Error writing to file {self.filename}: {e}")
            return False
        except Exception as e:
            print(f"✗ Unexpected error saving file: {e}")
            return False
    
    def add_student(self, name, student_id, test_1, test_2, test_3):
        """Add a new student to the system with all three scores and error handling."""
        if not name or not student_id:
            print("✗ Name and Student ID cannot be empty!")
            return False
        
        if student_id in self.students:
            print(f"✗ Student ID '{student_id}' already exists!")
            return False
        
        student = Student(name, student_id)
        
        if not student.add_test_1(test_1):
            print(f"✗ Invalid Test 1 score! Must be between 0 and 100.")
            return False
        if not student.add_test_2(test_2):
            print(f"✗ Invalid Test 2 score! Must be between 0 and 100.")
            return False
        if not student.add_test_3(test_3):
            print(f"✗ Invalid Test 3 score! Must be between 0 and 100.")
            return False
        
        self.students[student_id] = student
        print(f"✓ Student '{name}' added successfully!")
        print(f"  Scores: {test_1:.2f}, {test_2:.2f}, {test_3:.2f}")
        print(f"  Average: {student.average:.2f} | Grade: {student.grade}")
        self.save_to_file()
        return True
    
    def display_student(self, student_id):
        """Display information for a specific student with error handling."""
        if not student_id:
            print("✗ Student ID cannot be empty!")
            return False
        if student_id not in self.students:
            print(f"✗ Student ID '{student_id}' not found!")
            return False
        self.students[student_id].display_info()
        return True
    
    def search_by_name(self, name):
        """Search for students by name (case-insensitive) with formatted scores."""
        if not name:
            print("✗ Search name cannot be empty!")
            return
        
        search_name = name.lower()
        results = [s for s in self.students.values() if search_name in s.name.lower()]
        
        if not results:
            print(f"✗ No students found matching '{name}'")
            return
        
        print(f"\n{'='*95}")
        print(f"Search Results for '{name}' ({len(results)} match(es)):")
        print(f"{'='*95}")
        print(f"{'Name':<20} {'ID':<10} {'Test1':<10} {'Test2':<10} {'Test3':<10} {'Average':<10} {'Grade':<8}")
        print(f"{'='*95}")
        
        for student in results:
            test1 = f"{student.test_1:.2f}" if student.test_1 is not None else "N/A"
            test2 = f"{student.test_2:.2f}" if student.test_2 is not None else "N/A"
            test3 = f"{student.test_3:.2f}" if student.test_3 is not None else "N/A"
            
            if student.average is not None:
                avg = f"{student.average:.2f}"
            else:
                avg = "Pending"
            
            grade = student.grade if student.grade is not None else "Pending"
            print(f"{student.name:<20} {student.id:<10} {test1:<10} {test2:<10} {test3:<10} {avg:<10} {grade:<8}")
        
        print(f"{'='*95}\n")
    
    def display_all_students(self):
        """Display information for all students with scores formatted to 2 decimal places."""
        if not self.students:
            print("\n✗ No students in the system.")
            return
        
        print(f"\n{'='*95}")
        print(f"{'Name':<20} {'ID':<10} {'Test1':<10} {'Test2':<10} {'Test3':<10} {'Average':<10} {'Grade':<8}")
        print(f"{'='*95}")
        
        for student in self.students.values():
            test1 = f"{student.test_1:.2f}" if student.test_1 is not None else "N/A"
            test2 = f"{student.test_2:.2f}" if student.test_2 is not None else "N/A"
            test3 = f"{student.test_3:.2f}" if student.test_3 is not None else "N/A"
            
            if student.average is not None:
                avg = f"{student.average:.2f}"
            else:
                avg = "Pending"
            
            grade = student.grade if student.grade is not None else "Pending"
            print(f"{student.name:<20} {student.id:<10} {test1:<10} {test2:<10} {test3:<10} {avg:<10} {grade:<8}")
        
        print(f"{'='*95}\n")
    
    def calculate_class_statistics(self):
        """Calculate and display class statistics with formatted scores."""
        if not self.students:
            print("\n✗ No students in the system.")
            return
        
        students_with_scores = [s for s in self.students.values() if s.all_scores_entered()]
        
        if not students_with_scores:
            print("\n✗ No students have all three test scores entered yet.")
            return
        
        averages = [s.average for s in students_with_scores]
        class_avg = sum(averages) / len(averages)
        highest_avg = max(averages)
        lowest_avg = min(averages)
        
        # Find students with highest and lowest averages
        highest_student = [s for s in students_with_scores if s.average == highest_avg][0]
        lowest_student = [s for s in students_with_scores if s.average == lowest_avg][0]
        
        print(f"\n{'='*55}")
        print("CLASS STATISTICS")
        print(f"{'='*55}")
        print(f"Total Students: {len(self.students)}")
        print(f"Students with Complete Scores: {len(students_with_scores)}")
        print(f"Class Average: {class_avg:.2f}")
        print(f"Highest Average: {highest_avg:.2f} ({highest_student.name})")
        print(f"Lowest Average: {lowest_avg:.2f} ({lowest_student.name})")
        print(f"{'='*55}\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*55)
    print("STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*55)
    print("1. Add a new student")
    print("2. View student record (by ID)")
    print("3. Search student by name")
    print("4. View all students")
    print("5. View class statistics")
    print("6. Exit (or press Ctrl+C)")
    print("="*55)


def add_multiple_students(manager):
    """Function to add multiple students in one session."""
    print("\n" + "="*55)
    print("ADD STUDENT(S)")
    print("="*55)
    print("Enter 'done' for any field to finish adding students.\n")
    
    while True:
        try:
            name = input("Enter student name (or 'done' to exit): ").strip()
            if name.lower() == 'done':
                break
            if not name:
                print("✗ Name cannot be empty!\n")
                continue
            
            student_id = input("Enter student ID: ").strip()
            if not student_id:
                print("✗ Student ID cannot be empty!\n")
                continue
            
            try:
                test_1 = float(input("Enter Test 1 score (0-100): "))
                test_2 = float(input("Enter Test 2 score (0-100): "))
                test_3 = float(input("Enter Test 3 score (0-100): "))
                
                manager.add_student(name, student_id, test_1, test_2, test_3)
                print()  # Blank line for clarity
            except ValueError:
                print("✗ Invalid input! Please enter valid numbers for test scores.\n")
        except KeyboardInterrupt:
            print("\n✗ Student entry cancelled.\n")
            break


def view_student_record(manager):
    """Function to view a specific student record."""
    try:
        student_id = input("\nEnter student ID: ").strip()
        manager.display_student(student_id)
    except KeyboardInterrupt:
        print("\n✗ Operation cancelled.\n")


def search_students(manager):
    """Function to search for students by name."""
    try:
        search_name = input("\nEnter student name (or part of it): ").strip()
        if search_name:
            manager.search_by_name(search_name)
        else:
            print("✗ Search name cannot be empty!")
    except KeyboardInterrupt:
        print("\n✗ Search cancelled.\n")


def main():
    """Main program loop with improved organization and error handling."""
    manager = StudentRecordManager()
    
    # Load student records from file on startup
    print("="*55)
    print("STUDENT RECORDS MANAGEMENT SYSTEM")
    print("="*55)
    manager.load_from_file()
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
        except KeyboardInterrupt:
            # Handle Ctrl+C
            choice = '6'
        
        if choice == '1':
            add_multiple_students(manager)
        
        elif choice == '2':
            view_student_record(manager)
        
        elif choice == '3':
            search_students(manager)
        
        elif choice == '4':
            manager.display_all_students()
        
        elif choice == '5':
            manager.calculate_class_statistics()
        
        elif choice == '6':
            print("\n" + "="*55)
            print("Saving records and exiting...")
            print("="*55)
            if manager.save_to_file():
                print("✓ Records saved successfully!")
            print("\nThank you for using the Student Records Management System!")
            break
        
        else:
            print("✗ Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
