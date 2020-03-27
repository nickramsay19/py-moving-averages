class utils:

    @staticmethod
    def float_range(precision: int, min: int or float = 0, max: int or float = 1, inclusive: bool = False) -> list:
        """Returns a list of floats of certain precision within a defined range."""

        # Check that the parameters are the correct type and value.
        if type(precision) != int: raise TypeError('\'precision\' must be of type int.')
        elif precision < 1 or precision > 8: raise ValueError('\'precision\' must be between 1 and 8.')
        elif type(min) != int and type(min) != float: raise TypeError('\'min\' must be of type int or float.')
        elif type(max) != int and type(max) != float: raise TypeError('\'max\' must be of type int or float.')
        elif type(inclusive) != bool: raise TypeError('\'inclusive\' must be of type bool.')

        # Return the result of a list comprehension.
        return [float(x) / 10**precision for x in range(int(min * (10**precision)), int(max * (10**precision) + int(inclusive)))]

    @staticmethod
    def map2range(value: int or float, inMin: int or float, inMax: int or float, outMin: int or float, outMax: int or float) -> int or float:
        """Returns a mapped value to a new range."""

        # Check that the parameters are the correct type and value.
        if type(value) != int and type(value) != float: raise TypeError('\'value\' must be of type int or float.')
        elif type(inMin) != int and type(inMin) != float: raise TypeError('\'inMin\' must be of type int or float.')
        elif type(inMax) != int and type(inMax) != float: raise TypeError('\'inMax\' must be of type int or float.')
        elif type(outMin) != int and type(outMin) != float: raise TypeError('\'outMin\' must be of type int or float.')
        elif type(outMax) != int and type(outMax) != float: raise TypeError('\'outMax\' must be of type int or float.')
        elif value < inMin or value > inMax: raise ValueError('\'value\' must be in the range of \'inMin\' and \'inMax\'.')


        # Return and map the value
        return outMin + (float(value - inMin) / float(inMax - inMin) * outMax - outMin)

    @staticmethod
    def standard_deviation_population(data: list) -> float:
        """
        Returns the standard deviation of data from a population.
        :type data: list of int
        """

        # Check that the parameters are the correct type and value
        if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
        elif len(data) > 0:
            if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

        return (lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)))**(1/2))(data)

    @staticmethod
    def standard_deviation_sample(data: list) -> float:
        """
        Returns the standard deviation of data from a sample.

        :type data: list of int
        """

        # Check that the parameters are the correct type and value
        if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
        elif len(data) > 0:
            if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

        return (lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)-1))**(1/2))(data)

    @staticmethod
    def mean(data: list) -> float:
        """
        Returns the standard deviation of a set of values

        :type data: list of int
        """

        # Check that the parameters are the correct type and value
        if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
        elif len(data) > 0:
            if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

        return (lambda d : sum(n for n in d)/len(d))(data)

    @classmethod
    def standardise_population_data(cls, data: list) -> list:
        """
            Converts each value of a set of population values to their coressponding z-scores.

            :type data: list of int
        """

        # Check that the parameters are the correct type and value
        if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
        elif len(data) > 0:
            if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

        return (lambda d : [(n - cls.mean(d))/cls.standard_deviation_population(d) for n in d])(data)

    @classmethod
    def standardise_sample_data(cls, data: list) -> list:
        """
            Converts each value of a set of sample values to their coressponding z-scores.

            :type data: list of int
        """

        # Check that the parameters are the correct type and value
        if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
        elif len(data) > 0:
            if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

        return (lambda d : [(n - cls.mean(d))/cls.standard_deviation_sample(d) for n in d])(data)
