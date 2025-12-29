
        // --- Date Calculation Logic (New) ---
        function calculateTimingDate(config, baseDateStr) {
            if (!config) return '-';
            
            // If absolute, return date directly
            if (config.mode === 'absolute') {
                return config.date ? config.date.replace(/-/g, '.') : '-';
            }
            
            // If relative, and we have a base date
            if (config.mode === 'relative' && baseDateStr && baseDateStr !== '-') {
                // Parse base date (assume YYYY.MM.DD or YYYY-MM-DD)
                const standardizedDate = baseDateStr.replace(/\./g, '-');
                const base = new Date(standardizedDate);
                if (isNaN(base.getTime())) return '-';
                
                // Add months
                let monthsToAdd = parseInt(config.month || 0);
                if (isNaN(monthsToAdd)) monthsToAdd = 0;
                
                const targetDate = new Date(base.getFullYear(), base.getMonth() + monthsToAdd, 1);
                
                // Set day
                let day = parseInt(config.day);
                if (isNaN(day)) {
                    // unexpected day format
                     if (config.day === 'wage_payment_date') day = 15; // default or from settings?
                     else day = 99;
                }
                
                if (day === 99) {
                    // End of month
                    targetDate.setMonth(targetDate.getMonth() + 1);
                    targetDate.setDate(0);
                } else {
                    targetDate.setDate(day);
                }
                
                // Format YYYY.MM.DD
                const y = targetDate.getFullYear();
                const m = String(targetDate.getMonth() + 1).padStart(2, '0');
                const d = String(targetDate.getDate()).padStart(2, '0');
                return `${y}.${m}.${d}`;
            }
            
            return '-'; // Cannot calculate
        }
