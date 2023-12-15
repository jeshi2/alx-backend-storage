-- Create a temporary table to store the aggregated fan counts for each origin
CREATE TEMPORARY TABLE IF NOT EXISTS temp_fans_count AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the country origins based on the number of (non-unique) fans
SELECT origin, nb_fans
FROM temp_fans_count
ORDER BY nb_fans DESC;