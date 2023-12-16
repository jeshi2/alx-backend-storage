# MySQL advanced

This README provides an overview of a series of SQL tasks, including the scripts and stored procedures, along with explanations of how they work.

## Table of Contents

1. [Introduction](#introduction)
2. [Tasks Overview](#tasks-overview)
3. [Task Details](#task-details)
    - [Task 1: Metal Bands Analysis](#task-1-metal-bands-analysis)
    - [Task 2: Glam Rock Bands](#task-2-glam-rock-bands)
    - [Task 3: Update Items Quantity Trigger](#task-3-update-items-quantity-trigger)
    - [Task 4: Bonus Corrections Trigger](#task-4-bonus-corrections-trigger)
    - [Task 5: Validate Email Trigger](#task-5-validate-email-trigger)
    - [Task 6: Add Bonus Stored Procedure](#task-6-add-bonus-stored-procedure)
    - [Task 7: Compute Average Score For User Stored Procedure](#task-7-compute-average-score-for-user-stored-procedure)
    - [Task 8: Index on Names Table](#task-8-index-on-names-table)
    - [Task 9: Index on Names Table with Score](#task-9-index-on-names-table-with-score)
    - [Task 10: SafeDiv Function](#task-10-safediv-function)
    - [Task 11: Need Meeting View](#task-11-need-meeting-view)
    - [Task 100: Compute Average Weighted Score For User](#task-100-compute-average-weighted-score-for-user)
    - [Task 101: Compute Average Weighted Score For Users](#task-101-compute-average-weighted-score-for-users)
4. [How to Use](#how-to-use)
5. [Conclusion](#conclusion)

## Introduction

This set of tasks covers various aspects of SQL, including basic queries, triggers, stored procedures, views, and indexing. Each task is designed to address specific scenarios commonly encountered in database management.

## Tasks Overview

### Task 1: Metal Bands Analysis

**Script:** [metal_bands.sql.zip](tasks/1-metal-bands/metal_bands.sql.zip)

This task involves analyzing metal bands data, including finding the origin with the most fans.

### Task 2: Glam Rock Bands

**Script:** [3-glam_rock.sql](tasks/2-glam-rock/3-glam_rock.sql)

The task involves writing a script to list glam rock bands ranked by their longevity based on the provided table dump.

### Task 3: Update Items Quantity Trigger

**Scripts:** [4-init.sql](tasks/3-update-items-quantity-trigger/4-init.sql), [4-store.sql](tasks/3-update-items-quantity-trigger/4-store.sql), [4-main.sql](tasks/3-update-items-quantity-trigger/4-main.sql)

This task creates a trigger that decreases the quantity of an item after adding a new order.

### Task 4: Bonus Corrections Trigger

**Scripts:** [5-init.sql](tasks/4-bonus-corrections-trigger/5-init.sql), [5-valid_email.sql](tasks/4-bonus-corrections-trigger/5-valid_email.sql), [5-main.sql](tasks/4-bonus-corrections-trigger/5-main.sql)

The task involves creating a trigger that resets the `valid_email` attribute only when the email has been changed.

### Task 5: Validate Email Trigger

**Scripts:** [5-init.sql](tasks/5-validate-email-trigger/5-init.sql), [5-valid_email.sql](tasks/5-validate-email-trigger/5-valid_email.sql), [5-main.sql](tasks/5-validate-email-trigger/5-main.sql)

This task creates a trigger that resets the `valid_email` attribute only when the email has been changed.

### Task 6: Add Bonus Stored Procedure

**Scripts:** [6-init.sql](tasks/6-add-bonus-stored-procedure/6-init.sql), [6-bonus.sql](tasks/6-add-bonus-stored-procedure/6-bonus.sql), [6-main.sql](tasks/6-add-bonus-stored-procedure/6-main.sql)

The task involves creating a stored procedure named `AddBonus` that adds a new correction for a student.

### Task 7: Compute Average Score For User Stored Procedure

**Scripts:** [7-init.sql](tasks/7-compute-average-score-for-user-stored-procedure/7-init.sql), [7-average_score.sql](tasks/7-compute-average-score-for-user-stored-procedure/7-average_score.sql), [7-main.sql](tasks/7-compute-average-score-for-user-stored-procedure/7-main.sql)

This task creates a stored procedure named `ComputeAverageScoreForUser` that computes and stores the average score for a student.

### Task 8: Index on Names Table

**Scripts:** [names.sql.zip](tasks/8-index-on-names-table/names.sql.zip), [8-index_my_names.sql](tasks/8-index-on-names-table/8-index_my_names.sql)

The task involves creating an index `idx_name_first` on the `names` table for the first letter of the `name` column.

### Task 9: Index on Names Table with Score

**Scripts:** [names.sql.zip](tasks/9-index-on-names-table-with-score/names.sql.zip), [9-index_name_score.sql](tasks/9-index-on-names-table-with-score/9-index_name_score.sql)

This task creates an index `idx_name_first_score` on the `names` table for the first letter of the `name` and `score` columns.

### Task 10: SafeDiv Function

**Scripts:** [10-init.sql](tasks/10-safediv-function/10-init.sql), [10-div.sql](tasks/10-safed

iv-function/10-div.sql)

This task involves creating a function named `SafeDiv` that divides the first number by the second number or returns 0 if the second number is equal to 0.

### Task 11: Need Meeting View

**Scripts:** [11-init.sql](tasks/11-need-meeting-view/11-init.sql), [11-need_meeting.sql](tasks/11-need-meeting-view/11-need_meeting.sql), [11-main.sql](tasks/11-need-meeting-view/11-main.sql)

The task creates a view named `need_meeting` that lists all students needing a meeting based on score and last meeting date.

### Task 100: Compute Average Weighted Score For User

**Scripts:** [100-init.sql](tasks/100-compute-average-weighted-score-for-user/100-init.sql), [100-average_weighted_score.sql](tasks/100-compute-average-weighted-score-for-user/100-average_weighted_score.sql), [100-main.sql](tasks/100-compute-average-weighted-score-for-user/100-main.sql)

This task involves creating a stored procedure named `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student.

### Task 101: Compute Average Weighted Score For Users

**Scripts:** [101-init.sql](tasks/101-compute-average-weighted-score-for-users/101-init.sql), [101-average_weighted_score.sql](tasks/101-compute-average-weighted-score-for-users/101-average_weighted_score.sql), [101-main.sql](tasks/101-compute-average-weighted-score-for-users/101-main.sql)

This task involves creating a stored procedure named `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students.

## How to Use

1. **Import SQL Scripts:**
   ```bash
   $ cat <script_file_name> | mysql -uroot -p holberton
   ```

2. **Test Stored Procedures:**
   ```bash
   $ cat <test_script_file_name> | mysql -uroot -p holberton
   ```

## Conclusion

This set of SQL tasks covers a wide range of scenarios and database management concepts, including triggers, stored procedures, views, indexing, and functions. Each task is designed to enhance understanding and proficiency in SQL database operations.

**Author**
Antony Wagwana