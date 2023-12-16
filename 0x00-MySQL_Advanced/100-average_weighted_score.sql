-- Create a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;

    -- Calculate total weighted score and total weight for the user
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_weighted_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = p_user_id;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = CASE WHEN total_weight > 0 THEN total_weighted_score / total_weight ELSE 0 END
    WHERE id = p_user_id;
END //

DELIMITER ;