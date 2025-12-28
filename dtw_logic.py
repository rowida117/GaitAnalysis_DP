import numpy as np


class GaitAnalysisLogic:
    """
    this class does the main math for the app
    it makes the fake walking data and compares the signals
    """

    def generate_data(self, case_type):
        """
        makes fake sensor data to show walking
        it gives back a healthy signal and a patient signal
        """
        # make the healthy walking signal
        # using 4*pi to show 2 full steps
        # 100 dots is enough detail
        t_healthy = np.linspace(0, 4 * np.pi, 100)
        healthy = np.sin(t_healthy)

        if case_type == "match":
            # case 1: healthy match
            # this is a normal person
            # speed is the same as the healthy one
            t_patient = t_healthy
            # add a little bit of random noise to look real
            patient = np.sin(t_patient) + 0.05 * np.random.normal(size=len(t_patient))

        elif case_type == "slow":
            # case 2: slow walker
            # maybe an old person or hurt leg
            # takes longer to finish walking
            # i added more dots so it looks slower
            t_patient = np.linspace(0, 4 * np.pi, 140)

            # made the wave smaller cause muscles are weak
            patient = 0.8 * np.sin(t_patient) + 0.1 * np.random.normal(size=len(t_patient))



        elif case_type == "severe":
                    # case 3: really bad walking
                    # speed goes fast then slow
                    t_patient = np.linspace(0, 4 * np.pi, 140)
        
                    # changing the wave shape a lot
                    # looks like a limp or dragging a foot
                    patient = np.sin(t_patient * 1.5 + 1) + 0.2 * np.random.normal(size=len(t_patient))
        
                elif case_type == "tremor":
                    # case 4: parkinsons tremor
                    # the walking speed is normal but they are shaking
                    t_patient = t_healthy
        
                    # added a fast vibration wave on top of the walking
                    # using 10*t makes it shake really fast
                    tremor_noise = 0.15 * np.sin(10 * t_patient)
        
                    # combine the walk plus the shake plus noise
                    patient = np.sin(t_patient) + tremor_noise + 0.05 * np.random.normal(size=len(t_patient))
        
                else:
                    # just in case something breaks
                    raise ValueError("unknown case type selected")
        return healthy, patient

    def compute_dtw(self, s1, s2):
        """
        this is the main dtw tool
        it finds the best match between two waves
        """
        n, m = len(s1), len(s2)

        # 1. set up the grid
        # we need a box of size n+1 by m+1
        # filling it with big numbers first
        dp = np.full((n + 1, m + 1), np.inf)

        # start point has zero cost
        dp[0, 0] = 0

        # 2. fill the grid
        # check every row and column
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # find distance between two dots
                cost = abs(s1[i - 1] - s2[j - 1])

                # look at neighbors to find the cheapest path
                # diagonal is a match
                # up is adding a step
                # left is skipping a step
                dp[i, j] = cost + min(
                    dp[i - 1, j - 1],
                    dp[i - 1, j],
                    dp[i, j - 1]
                )

        # 3. trace back the best path
        # start from the end corner
        path = []
        i, j = n, m

        #continue here
        return dp, path

    def stress_test(self):
        """
        just checking if it crashes on big data
        """
        print("running stress test...")
        # make huge random lists
        big_s1 = np.random.rand(1000)
        big_s2 = np.random.rand(1200)
        try:
            # might be slow cause math is heavy
            dp, path = self.compute_dtw(big_s1, big_s2)
            print(f"test passed matrix size: {dp.shape} path length: {len(path)}")
            return True
        except Exception as e:
            print(f"test failed: {e}")
            return False
