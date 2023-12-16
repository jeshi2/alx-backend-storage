-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_projects INT;

    -- Calculate total score and number of projects for the user
    SELECT SUM(score), COUNT(*) INTO total_score, num_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Update the average score for the user
    UPDATE users
    SET average_score = IFNULL(total_score / NULLIF(num_projects, 0), 0)
    WHERE id = user_id;
END;
//
DELIMITER ;