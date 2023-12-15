-- Create a temporary table to store bands with Glam rock as their main style
CREATE TEMPORARY TABLE IF NOT EXISTS temp_glam_rock_bands AS
SELECT
    band_name,
    YEAR('2022-01-01') - CAST(SUBSTRING_INDEX(lifespan, ' - ', -1) AS SIGNED) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock';

-- List Glam rock bands ranked by their longevity
SELECT
    band_name,
    lifespan
FROM
    temp_glam_rock_bands
ORDER BY
    lifespan DESC;