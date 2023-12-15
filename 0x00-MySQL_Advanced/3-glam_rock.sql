-- List Glam rock bands ranked by their longevity
SELECT
    band_name,
    YEAR('2022-01-01') - CAST(SUBSTRING_INDEX(lifespan, ' - ', -1) AS SIGNED) AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;